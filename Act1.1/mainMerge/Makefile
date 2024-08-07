# Variables
CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++11
TARGET = merge_sort
SRC = main.cpp
OBJ = $(SRC:.cpp=.o)
TESTS = test_cases.txt
OUTPUT = output.txt

# Regla por defecto
all: $(TARGET)

# Regla para compilar el objetivo
$(TARGET): $(OBJ)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(OBJ)

# Regla para compilar archivos objeto
%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $<

# Regla para ejecutar pruebas
test: $(TARGET)
	@echo "Running test cases..."
	./$(TARGET) < $(TESTS) > $(OUTPUT)
	@echo "Output stored in $(OUTPUT)"
	@cat $(OUTPUT)

# Regla para limpiar archivos generados
clean:
	rm -f $(OBJ) $(TARGET) $(OUTPUT)

# Regla para limpiar todo, incluyendo archivos de prueba
distclean: clean
	rm -f $(TESTS)
