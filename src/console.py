import datetime
from query_bucket.athena_boto import *

def lambda_handler(event, context):
    time = datetime.datetime.now().strftime("%d.%b %Y %H:%M:%S")
    
    output_bucket_name = "jigsawtexasresults" # change to your output bucket
    db_name = "txreceipts" # change to your db
    output_folder = "output" 
    query = "SELECT * FROM jigsawtexasquery limit 3"
    output_bucket_folder = f"s3://{output_bucket_name}/{output_folder}/"
    
    print('called at', time)
    query_response = query_athena(query,
                               db_name, output_bucket_folder)
    
    results_df = get_query_results(output_bucket_name, output_folder, query_response)
    print(results_df)
    return results_df.to_dict('records')

# change jigsawtexasquery to your input bucket
# query_results("SELECT * FROM jigsawtexasquery limit 3")