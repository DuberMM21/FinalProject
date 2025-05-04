from api.dependencies import Base, engine
import api.models

# Create all tables in the database
Base.metadata.create_all(bind=engine)

print("All tables created successfully.")
