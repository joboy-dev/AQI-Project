from data import data_scraper
from ML import model_training

# Run scrape function
data_scraper.scrape_aqi_data()

# Train model
model_training.train_model()
