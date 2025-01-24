from crewai.flow.flow import Flow, listen, or_, start

class OrExampleFlow(Flow):

    @start()
    def start_method(self):
        print("Starting flow")
        return "Hello from the start method"

    @listen(start_method)
    def second_method(self):
        print("Second method")
        return "Hello from the second method"

    @listen(or_(start_method, second_method))
    def logger(self, result):
        print(f"Logger: {result}")
    # will wait for one flows and then trigger and then trigger again when the other flow is done


flow = OrExampleFlow()
flow.kickoff()