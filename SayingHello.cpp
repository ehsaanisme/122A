#include <iostream>
#include <sstream>
#include <string>

void hello(const std:: string& name){
    std::cout << "Hello " << name << "!\n";
}

int main() {
    std::string roster = "Ben Srikkanth Anna Additya Ben";

    std::stringstream ss(roster);
    std::string name;

    while(ss >> name) {
        hello(name);
    }

    return 0;
}