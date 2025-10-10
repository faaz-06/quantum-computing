# quantum-computing
Solution to the Problem Statement for QC Club Inductions
Section -2 PS-1

Creating a library that simulats libraries like Qiskit, Pennylane, etc.

1. To apply single qubit gates like X gate, Y gate, etc. on a 1-qubit system just call the function corresponding to the gate with the argument as a qubit that is to be represented by a list.
2. To apply 2 qubit gates like CXgate and CYgate on a 2 qubit system, we can use the corresponding functions with the arguments in the order-control qubit,target qubit
3. To create a register of multiple qubits, we can use the function tensor_prod, where we have to register the qubit to the system one by one. i.e, we have to first create a register of 2 qubits, then use tensor product again to create a register of 3 qubits.
4. The function quantumregister creates a statevector of n-dimensions of the form |00000.....n>
5. The single_qubit_gate function is used to apply a single qubit gate to a qubit in a multi-qubit system.
6. The showstate function allows us to view the statevector, and the measure function allows us to measure the whole system.
