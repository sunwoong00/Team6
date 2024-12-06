import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

class RetrievalEngine:
    def __init__(self, demo_data_path: str = '/home/sanghyun/file/unid/new_infor.json'):
        self.naturalFormat = True
        with open(demo_data_path, 'r') as f:
            self.demo_set = json.load(f)
        self.sentence_embedder = SentenceTransformer("all-MiniLM-L12-v2")

    def single_retrieval(self, query, category=None):
        query_emb = self.sentence_embedder.encode([query])
        best_item = None
        best_dist = float('inf')
        
        # Loop through each category in the JSON file
        for cat, items in self.demo_set.items():
            if category and cat != category:
                continue  # Skip categories that don't match the specified category
            
            for item in items:
                # Combine fields into a single text to represent the item
                if cat == "노래":
                    item_text = f"{item['title']} by {item['artist']}"
                elif cat == "뉴스":
                    item_text = f"{item['title']} on {item['date']}"
                
                item_emb = self.sentence_embedder.encode([item_text])
                dist = 1 - cosine_similarity(query_emb, item_emb)[0][0]
                
                # Keep track of the best match
                if dist < best_dist:
                    best_dist = dist
                    best_item = (cat, item)  # Store both category and item for context
        
        return best_item  # Return the best matching item

    def search_demo(self, query, category=None):
        result_text = ''
        best_item = self.single_retrieval(query, category=category)

        if best_item:
            cat, item = best_item
            if cat == "노래":
                result_text = f"노래: {item['title']} by {item['artist']}"
            elif cat == "뉴스":
                result_text = f"뉴스: {item['title']} on {item['date']}"
        
        return result_text

# Example usage
if __name__ == "__main__":
    engine = RetrievalEngine(demo_data_path='/home/sanghyun/file/unid/new_infor.json')
    query = "노래"
    result = engine.search_demo(query, category="노래")
    print(result)
