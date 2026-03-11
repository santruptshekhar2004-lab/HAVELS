import time
from agents.orchestrator import create_orchestrator


def main():
    orchestrator = create_orchestrator()
    print("Agent Orchestrator (type 'quit' to exit)")
    print("Supports: Shopping queries | IoT device control")
    print("-" * 50)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() in ("quit", "exit"):
            break
        if not user_input:
            continue

        start = time.time()
        response = orchestrator(user_input)
        latency = (time.time() - start) * 1000
        print(f"\n[Latency: {latency:.0f}ms]")


if __name__ == "__main__":
    main()
