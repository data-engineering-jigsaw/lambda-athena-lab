from query_bucket.athena_boto import *

def query_results(query):
    output_bucket_name = "jigsawtexasresults" # change to your output bucket
    db_name = "txreceipts" # change to your db
    output_folder = "output" 
    
    output_bucket_folder = f"s3://{output_bucket_name}/{output_folder}/"
    query_response = query_athena(query,
                               db_name, output_bucket_folder)
    
    results_df = get_query_results(output_bucket_name, output_folder, query_response)
    return results_df

# change jigsawtexasquery to your input bucket
# query_results("SELECT * FROM jigsawtexasquery limit 3")