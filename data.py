CREATE TABLE Ingredients (
  ingredient_id INT PRIMARY KEY,
  name VARCHAR(50),
  unit VARCHAR(20),
  cost DECIMAL(10,2)  
);

CREATE TABLE Recipes (
  recipe_id INT PRIMARY KEY,
  product_id INT,
  ingredient_id INT, 
  quantity DECIMAL(10,2),
  FOREIGN KEY (product_id) REFERENCES Products(product_id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);

CREATE TABLE Inventory (
  inventory_id INT PRIMARY KEY,
  ingredient_id INT,
  quantity INT,
  location VARCHAR(100),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id)
);

CREATE TABLE Production (
  production_id INT PRIMARY KEY,
  bakery_id INT,
  product_id INT,
  production_date DATE,
  quantity INT,
  quality_score INT,
  FOREIGN KEY (bakery_id) REFERENCES Bakeries(bakery_id),
  FOREIGN KEY (product_id) REFERENCES Products(product_id) 
);

CREATE TABLE Reviews (
  review_id INT PRIMARY KEY, 
  customer_id INT,
  product_id INT,
  review_text VARCHAR(500),
  rating INT,
  FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
  FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

CREATE TABLE Topics (
  topic_id INT PRIMARY KEY,
  name VARCHAR(50)
);

CREATE TABLE ReviewTopics (
  review_id INT,
  topic_id INT,
  FOREIGN KEY (review_id) REFERENCES Reviews(review_id),
  FOREIGN KEY (topic_id) REFERENCES Topics(topic_id)
);

CREATE TABLE Reviews (
  review_id INT PRIMARY KEY,
  customer_id INT, 
  review_text TEXT,
  FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Ingredients (
  ingredient_id INT PRIMARY KEY,
  name VARCHAR(50),
  unit VARCHAR(20),
  cost DECIMAL(10,2)
);

CREATE TABLE ProductionLogs (
  log_id INTEGER PRIMARY KEY, 
  product_id INTEGER,
  bake_date TEXT,
  temperature REAL,
  pH REAL,
  FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

CREATE TABLE Microbiome (
  sample_id INTEGER PRIMARY KEY,
  product_id INTEGER, 
  bacteria TEXT,
  yeasts TEXT,
  mold TEXT,
  FOREIGN KEY(product_id) REFERENCES Products(product_id)
);

CREATE TABLE Reviews (
  review_id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  product_id INTEGER, 
  review_text TEXT,
  rating INTEGER,
  FOREIGN KEY(customer_id) REFERENCES Customers(customer_id), 
  FOREIGN KEY(product_id) REFERENCES Products(product_id)
);