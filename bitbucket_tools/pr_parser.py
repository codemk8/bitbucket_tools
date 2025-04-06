
def parse_pr_file_list(data):
    """
    Parse the BitBucket PR file list JSON data and return a list of dictionaries
    containing file paths and their status.
    
    Args:
        data (dict): The JSON data from BitBucket API
        
    Returns:
        list: A list of dictionaries with 'path' and 'status' keys
    """
    files = []
    
    for file_info in data.get('values', []):
        # Get the file path (if new exists use that, otherwise use old)
        if file_info.get('new'):
            path = file_info['new'].get('path')
        else:
            path = file_info['old'].get('path')
            
        # Get the status (modified, removed, added)
        status = file_info.get('status')
        
        # Get lines added/removed for additional info
        lines_added = file_info.get('lines_added', 0)
        lines_removed = file_info.get('lines_removed', 0)
        
        files.append({
            'path': path,
            'status': status,
            'lines_added': lines_added,
            'lines_removed': lines_removed
        })
    
    return files