# Variables
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++11 -MMD -MP
LDFLAGS = 
TARGET = sort_students
SRC = main.cpp
OBJ = $(SRC:.cpp=.o)
DEPS = $(OBJ:.o=.d)
TESTS = test_cases.txt
OUTPUT = output.txt
EXPECTED_OUTPUT = expected_output.txt

# Regla por defecto para compilar el programa
all: $(TARGET)

# Regla para compilar el objetivo
$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJ) $(LDFLAGS)

# Regla para compilar archivos objeto
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

# Incluir dependencias de archivos generados automáticamente
-include $(DEPS)

# Regla para limpiar archivos generados
clean:
	rm -f $(OBJ) $(DEPS) $(TARGET) $(OUTPUT)

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
	@diff -w $(OUTPUT) $(EXPECTED_OUTPUT) && echo "Test passed!" || echo "Test failed!"