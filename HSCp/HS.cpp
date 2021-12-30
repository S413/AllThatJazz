#include<pybind11/pybind11.h>
#include<pybind11/stl.h>
#include<pybind11/operators.h>
#include<pybind11/embed.h>

#include<iostream>
#include<vector>
#include<stdexcept>
#include<iomanip>

namespace py = pybind11;

//HarmonyMemory

class HarmonyMemory {
	
public:
	HarmonyMemory() : m_HMS(0), m_N(0) { initHM(0,0); }

	HarmonyMemory(size_t HMS, size_t N): m_HMS(HMS), m_N(N){
		initHM(HMS, N);
	}

	HarmonyMemory(size_t HMS, size_t N, std::vector<double> const& vec)
		: m_HMS(HMS), m_N(N)
	{
		initHM(HMS, N);
		
		size_t k = 0;
		for (size_t i = 0; i < m_HMS; ++i) {
			for (size_t j = 0; j < m_N; ++j) {
				(*this)(i, j) = vec[k];
				++k;
			}
		}
	}

	HarmonyMemory& operator=(const HarmonyMemory& other) {
		if (this == &other) { return *this; }

		if (m_HMS != other.m_HMS || m_N != other.m_N) {
			initHM(other.m_HMS, other.m_N);
		}

		for (size_t i = 0; i < m_HMS; ++i) {
			for (size_t j = 0; j < m_N; ++j) {
				(*this)(i, j) = other(i, j);
			}
		}

		return *this;
	}

	HarmonyMemory(const HarmonyMemory& other): m_HMS(other.m_HMS), m_N(other.m_N) {
		initHM(other.m_HMS, other.m_N);

		for (size_t i = 0; i < other.m_HMS; ++i) {
			for (size_t j = 0; j < m_N; ++j) {
				(*this)(i, j) = other(i, j);
			}
		}
	}

	HarmonyMemory& operator=(std::vector<double> const& vec) {
		if (size() != vec.size()) {
			throw std::out_of_range("Sizes do not match.");
		}

		size_t k = 0;

		for (size_t i = 0; i < m_HMS; ++i) {
			for (size_t j = 0; j < m_N; ++j) {
				(*this)(i, j) = vec[k];
				++k;
			}
		}

		return *this;
	}

	~HarmonyMemory() {
		initHM(0, 0);
	}

	size_t index(size_t HMS, size_t N) const { return HMS * m_N + N; }
	size_t size() const { return m_HMS * m_N; }
	size_t HMS() const { return m_HMS; }
	size_t N() const { return m_N; }

	double buffer(size_t i) const { return m_buffer[i]; }

	std::vector<double> buffer_vector() const { return std::vector<double>(m_buffer, m_buffer + size()); }

	double operator()(size_t HMS, size_t N) const { 
		if (checkbounds(HMS, N)) {
			throw std::out_of_range("Index out of bounds.");
		}
		return m_buffer[index(HMS, N)]; 
	}

	double& operator()(size_t HMS, size_t N) { 
		if (checkbounds(HMS, N)) {
			throw std::out_of_range("Index out of bounds.");
		}
		return m_buffer[index(HMS, N)]; 
	}

	double operator[](size_t idx) const {
		if (idx > (m_HMS * m_N)-1) {
			throw std::out_of_range("Index out of bounds.");
		}
		return m_buffer[idx];
	}

	double& operator[](size_t idx) {
		if (idx > (m_HMS * m_N)-1) {
			throw std::out_of_range("Index out of bounds.");
		}
		return m_buffer[idx];
	}

	void initHM(size_t HMS, size_t N) {
		if (m_buffer) { delete[] m_buffer; }
		
		size_t nelements = HMS * N;

		if (nelements) { m_buffer = new double[nelements]; }
		else { m_buffer = nullptr; }

		m_HMS = HMS;
		m_N = N;
	}

	bool checkbounds(size_t HMS, size_t N) const {
		if (HMS > m_HMS || N > m_N) {
			return true;
		}

		return false;
	}

private:
	size_t m_HMS = 0;
	size_t m_N = 0;
	double* m_buffer = nullptr;
};

bool operator==(HarmonyMemory const& m1, HarmonyMemory const& m2) {
	if (m1.HMS() != m2.HMS() || m1.N() != m2.N()) {
		return false;
	}

	for (size_t i = 0; i < m1.HMS(); ++i) {
		for (size_t j = 0; j < m1.N(); ++j) {
			if (m1(i, j) != m2(i, j)) {
				return false;
			}
		}
	}

	return true;
}

//HarmonySearch
class HarmonySearch {
public:
	HarmonySearch(size_t HMS, size_t N, std::vector<std::pair<double, double>>x_dom, double HMCR=0.7, double PR=0.1) : m_HMCR(HMCR), m_PR(PR) {
		HarmonyMemory mem(HMS, N);

		for (size_t i = 0; i < HMS; ++i) {
			for (size_t j = 0; j < N; ++j) {
				//I have to initialize within constraints for Xi values
				double xij = x_dom[j].first + static_cast <double> (rand() / static_cast <double> (RAND_MAX / (x_dom[j].second - x_dom[j].first)));
				mem(i,j) = xij;
			}
		}

		mem0 = mem;
		constraints.resize(N);
		constraints = x_dom;
	}

	HarmonySearch(HarmonyMemory mem, std::vector<std::pair<double, double>>x_dom, double HMCR=0.7, double PR=0.1) : m_HMCR(HMCR), m_PR(PR) {
		//should assume it is full already
		//maybe check that the values are valid
		for(size_t i = 0; i < mem.HMS(); ++i){
			for(size_t j = 0; j < mem.N(); ++j){
				if(mem(i,j) > x_dom[j].second || mem(i,j) < x_dom[j].first){
					std::cout << "Warning. Some X values are outside set constraints." << std::endl;
				}
			}
		}

		constraints.resize(mem.N());
		constraints = x_dom;
		mem0 = mem;
	}
	
	void PyObjectiveFunc() {
		py::scoped_interpreter python;
		
		py::module objectFun = py::module::import("objectFun");
		py::object OF = objectFun.attr("ObjectiveFun"); 
	}
	
	void viewMemory() {
		std::cout << "Current Harmony Memory State:" << std::endl;

		for (size_t i = 0; i < mem0.HMS(); ++i) {
			for (size_t j = 0; j < mem0.N(); ++j) {
				std::cout << std::setprecision(3) << std::fixed << std::setw(6) << mem0(i, j) << std::setfill(' ') << "  ";
			}
			std::cout << std::endl;
		}
	}

	void viewConstraints() {
		for(size_t i = 0; i < constraints.size(); ++i){
			std::cout << constraints[i].first << ", " << constraints[i].second << std::endl;
		}
	}

	HarmonyMemory retrieveMem() { return mem0; }
	std::vector<std::pair<double,double>> retrieveCons() { return constraints; }
	double HMCR() const { return m_HMCR; }
	void HMCR(double val) { m_HMCR = val; }
	double PR() const { return m_PR; }
	void PR(double val) { m_PR = val; }

	double m_HMCR;
	double m_PR;
private:
	HarmonyMemory mem0;
	std::vector<std::pair<double,double>>constraints;
};

PYBIND11_MODULE(HSCp, m){
        py::class_<HarmonyMemory>(m, "HarmonyMemory")
	        .def(py::init<>())
	        .def(py::init<const size_t, const size_t>())
	        .def("__setitem__", [](HarmonyMemory &m, std::pair<size_t,size_t>ix, const double v){
			m(ix.first, ix.second) = v;
			}, py::is_operator())
                .def("__getitem__", [](HarmonyMemory &m, std::pair<size_t,size_t>ix){
			return m(ix.first,ix.second);
			}, py::is_operator())
	        .def_property_readonly("HMS", &HarmonyMemory::HMS)
		.def_property_readonly("N", &HarmonyMemory::N)
	        .def(py::self==py::self);

	py::class_<HarmonySearch>(m, "HarmonySearch")
                .def(py::init<size_t,size_t,std::vector<std::pair<double,double>>>())
		.def(py::init<HarmonyMemory, std::vector<std::pair<double,double>>>())
	        .def("viewMemory", &HarmonySearch::viewMemory)
		.def("viewConstraints", &HarmonySearch::viewConstraints)
		.def("retrieveMem", &HarmonySearch::retrieveMem)
		.def("retrieveCons", &HarmonySearch::retrieveCons)
		.def_readwrite("HMCR", &HarmonySearch::m_HMCR)
		.def_readwrite("PR", &HarmonySearch::m_PR);
}	


//have just made the most basic skeleton for HM
//still have to create Harmony Search Class, and polish HM class
