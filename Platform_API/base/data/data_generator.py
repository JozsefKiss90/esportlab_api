import random
import json


def generate_reaction_time_data(num_samples):
    data = []

    for _ in range(num_samples):
        rt = random.randint(200, 1000)
        acc = random.choice([50, 100])
        email = f"user_{_}@example.com"  # Generate a unique email address
        entry = {"rt": rt, "email": email, "acc": acc}
        data.append(entry)

    return data


def save_reaction_time_data_to_json(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# Generate reaction time data with 7 samples
reaction_time_data = generate_reaction_time_data(20)

# Save the data to a JSON file
file_path = "base/files/reaction_times.json"
save_reaction_time_data_to_json(reaction_time_data, file_path)
