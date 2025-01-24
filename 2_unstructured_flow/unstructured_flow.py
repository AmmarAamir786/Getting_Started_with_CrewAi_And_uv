from crewai.flow.flow import Flow, listen, start

class UntructuredExampleFlow(Flow):

    @start()
    def first_method(self):
        print("Starting flow") # Starting flow
        print(f"State before first_method:\n{self.state}")
        # State before first_method: 
        # {}
        self.state["message"] = "Hello from unstructured flow"
        self.state["counter"] = 0

    @listen(first_method)
    def second_method(self):
        print(f"State before second_method:\n{self.state}")
        # State before second_method:
        # {'message': 'Hello from unstructured flow', 'counter': 0}
        self.state["message"] += " - updated"
        self.state["counter"] += 1

    @listen(second_method)
    def third_method(self):
        print(f"State before third_method:\n{self.state}")
        # State before third_method:
        # {'message': 'Hello from unstructured flow - updated', 'counter': 1}
        self.state["message"] += " - updated again"
        self.state["counter"] += 1

        print(f"State after third_method:\n{self.state}")
        # State after third_method:
        # {'message': 'Hello from unstructured flow - updated - updated again', 'counter': 2}


flow = UntructuredExampleFlow()
flow.kickoff()

print(f"Final state:\n{flow.state}")
# Final state:
# {'message': 'Hello from unstructured flow - updated - updated again', 'counter': 2}