from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def generate_random_bits(num_bits):
    """
    Generate a random binary sequence using a quantum simulator.
    """
    simulator = AerSimulator()

    # Create a circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)

    # Put the qubit into superposition
    qc.h(0)

    # Measure the qubit
    qc.measure(0, 0)

    # Compile the circuit once
    compiled_circuit = transpile(qc, simulator)

    # Execute all shots in a single pass with individual memory tracking enabled
    job = simulator.run(compiled_circuit, shots=num_bits, memory=True)

    result = job.result()

    # Extract the sequence of measurement results
    memory = result.get_memory()

    return "".join(memory)

# Run only when this file is executed directly
if __name__ == "__main__":

    print("=" * 55)
    print(" Quantum Random Number Generator Simulator")
    print("=" * 55)

    bits = generate_random_bits(20)

    print("\nGenerated Random Binary Sequence:\n")
    print(bits)
    print("\nLength :", len(bits))