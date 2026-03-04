from agents.schedule_agent import create_schedule_agent
from utils.gmail_script import read_gmail_messages
def main():

    agent = create_schedule_agent()

    message = read_gmail_messages()

    result = agent.invoke({"message": message})

    print(result)


if __name__ == "__main__":
    main()