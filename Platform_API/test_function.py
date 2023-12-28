import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Platform_API.settings')
django.setup()

from Platform_API.base.stats.tests.correlation_hardcoded import correlation_hardcoded, pearson_scipy

#from base.graphs import t_test_table, cyberpunk_scatterplot, cyberpunk_graph, t_test_table_2
#generate_graph_from_file('./base/files/reaction_times.xlsx')


file_path = "base/files/reaction_times.json"

#generate_graph_from_json(file_path)

#def generate_reaction_time_json():
#    reaction_time_data = generate_reaction_time_data(50)
#    save_reaction_time_data_to_json(reaction_time_data, file_path)


#generate_reaction_time_json()
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]
print(correlation_hardcoded(x, y))
print(pearson_scipy(x,y))
