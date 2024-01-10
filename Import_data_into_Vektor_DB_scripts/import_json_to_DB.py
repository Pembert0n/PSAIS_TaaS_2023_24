#For Row based design (transcription.txt ist zwar keine json aber das ist wahrscheinlich das passende)
#wir können das von txt auf json ohne probleme ändern --suphi
from pymilvus import connections

# Connect to Milvus Docker container
connections.connect(host='localhost', port='19530')

from pymilvus import utility
task_id = utility.do_bulk_insert(
    collection_name="Podcast",
    partition_name="2023",
    files=["../knowledge_science_ep1_transcription.json"] #For a row-based JSON file, parameter files should be a one-member list containing the path to the JSON file.
)
