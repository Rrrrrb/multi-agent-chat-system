from agents.coordinator import Coordinator
import os

 

def interactive_mode():
    coordinator = Coordinator()
    print("=== Multi-Agent Chat System ===")
    print("Type 'exit' to quit")
    
    while True:
        query = input("\nYou: ")
        if query.lower() == "exit":
            break
        result = coordinator.handle_query(query)
        print(f"System: {result}")

if __name__ == "__main__":
    interactive_mode()




# for already written test cases
# if not os.path.exists("outputs"):
#     os.mkdir("outputs")

# def run_tests():
#     coordinator = Coordinator()

#     queries = [
#         "neural networks",
#         "transformers analyze",
#         "What did we discuss about neural networks earlier?",
#         "reinforcement learning analyze",
#         "compare neural networks"
#     ]

#     filenames = [
#         "outputs/simple_query.txt",
#         "outputs/complex_query.txt",
#         "outputs/memory_test.txt",
#         "outputs/multi_step.txt",
#         "outputs/collaborative.txt"
#     ]

#     for q, f in zip(queries, filenames):
#         result = coordinator.handle_query(q)
#         with open(f, "w") as file:
#             file.write(str(result))
#         print(f"[Main] Output saved to {f}")

# if __name__ == "__main__":
#     run_tests()
