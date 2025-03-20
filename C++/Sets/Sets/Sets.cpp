#include <iostream>
#include <list>
#include <tuple>
#include <bitset>
#include <chrono>

std::list <std::pair<int, int>> create_set(int n) {
	std::list <std::pair<int, int>> universal_set;

	for (int a = 0; a < n; a++) {
		for (int b = 0; b < n; b++) {
			universal_set.push_back(std::pair<int, int> (a, b));
		}
	}

	return universal_set;

}

bool is_transitive(std::list <std::pair<int, int>> subset) {

	for (std::pair<int, int> element1 : subset) {
		
		bool b_never_c = true;
		
		for (std::pair<int, int> element2 : subset) {

			if (element1.second == element2.first and (std::find(subset.begin(), subset.end(), (std::pair<int, int>(element1.first, element2.second)))) != subset.end()) {
			}
			else if (element1.second == element2.first) {
				b_never_c = false;
			}

		}

		if (not b_never_c) {
			return false;
		}
	
	}

	return true;

}

int check_subsets(int n, std::list<std::pair<int,int>> universal_set) {
	int transitive_relations = 0;

	for (int iter = 0; iter < std::pow(2, n * n); iter++) {
		std::string binary = std::bitset<64>(iter).to_string();
		std::string sub_binary = binary.substr(64 - (n * n), n*n);

		std::list<std::pair<int, int>> subset;
		int ind = 0;

		for (std::pair<int, int> element : universal_set) {
			if (int(sub_binary[ind])-48) {
				subset.push_back(element);
			}
			ind++;
		}

		transitive_relations += is_transitive(subset);

	}

	return transitive_relations;

}

int main() {

	auto start = std::chrono::high_resolution_clock::now();

	int n = 5;

	std::cout << check_subsets(n, create_set(n));

	auto end = std::chrono::high_resolution_clock::now();

	auto duration = std::chrono::duration_cast<std::chrono::seconds>(end - start).count();

	std::cout << "\nExecution time: " << duration << " s" << std::endl;

	return 0;
}