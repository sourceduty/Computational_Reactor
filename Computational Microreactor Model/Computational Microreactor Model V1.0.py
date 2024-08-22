class Microreactor:
    def __init__(self, V, A, B, C):
        self.reactants = {
            'V': V,
            'A': A,
            'B': B,
            'C': C,
            'S': 0,
            'F': 0,
            'E': 0,
            'W': 0
        }
        self.sensors = {
            'activation': 0,
            'process': [],
            'data': [],
            'io': [],
            'reaction': []
        }
    
    def initiate_reaction(self):
        # Step 1: Initiation
        self.reactants['V'] -= 10
        self.sensors['activation'] += 10
        self.sensors['process'].append("V decreased by 10 units")
    
    def reaction_A(self):
        # Step 2: A's Reaction
        self.reactants['A'] -= 5
        self.reactants['B'] += 5
        self.sensors['process'].append("A decreased by 5 units and B increased by 5 units")
    
    def reaction_B(self):
        # Step 3: B's Reaction
        self.reactants['B'] -= 10
        self.reactants['C'] += 10
        self.sensors['process'].append("B decreased by 10 units and C increased by 10 units")
    
    def reaction_C(self):
        # Step 4: C's Reaction
        self.reactants['C'] -= 15
        self.reactants['E'] += 10
        self.sensors['process'].append("C decreased by 15 units and E increased by 10 units")
    
    def termination(self):
        # Step 5: Termination
        self.reactants['C'] -= 10
        self.reactants['W'] += 10
        self.sensors['process'].append("C decreased by 10 units and W increased by 10 units")
    
    def run_simulation(self):
        self.initiate_reaction()
        self.reaction_A()
        self.reaction_B()
        self.reaction_C()
        self.termination()
    
    def report_final_state(self):
        print("Final States:")
        for reactant, amount in self.reactants.items():
            print(f"- {reactant} = {amount} units")
        
        print("\nSensor Readings:")
        print(f"- Activation Sensors: V activation decreased by {self.sensors['activation']} units")
        for process in self.sensors['process']:
            print(f"- Process Sensors: {process}")
        print("- Data Sensors: Changes in reactant concentrations observed.")
        print("- IO Sensors: Input of V and output of W measured.")
        print("- Reaction Sensors: Monitoring the progression from A to W.")
    

# Initial conditions as per the example:
V = 100
A = 50
B = 30
C = 20

# Create an instance of the Microreactor
reactor = Microreactor(V, A, B, C)

# Run the simulation
reactor.run_simulation()

# Report the final state of the system
reactor.report_final_state()
