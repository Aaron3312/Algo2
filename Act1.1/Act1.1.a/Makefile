# Variables
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++11
TARGET = merge_sort
SRC = main.cpp
HEADERS = *.h
OBJ = $(SRC:.cpp=.o)
TESTS = test_cases.txt
OUTPUT = output.txt

# Regla por defecto para compilar el programa
all: $(TARGET)

# Regla para compilar el objetivo
$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJ)

# Regla para compilar archivos objeto
%.o: %.cpp $(HEADERS)
	$(CXX) $(CXXFLAGS) -c $<

# Regla para limpiar archivos generados
clean:
	rm -f $(OBJ) $(TARGET) $(OUTPUT)

# Regla para limpiar y recompilar todo
rebuild: clean all

# Regla para ejecutar valgrind y verificar memory leaks
valgrind: $(TARGET)
	valgrind --leak-check=full ./$(TARGET)

# Regla para ejecutar pruebas
test: $(TARGET)
	@echo "Running test cases..."
	./$(TARGET) < $(TESTS) > $(OUTPUT)
	@echo "Output stored in $(OUTPUT)"
	@cat $(OUTPUT)