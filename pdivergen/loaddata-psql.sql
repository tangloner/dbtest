COPY customer FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/customer.csv' WITH (FORMAT csv, DELIMITER '|');
COPY nation FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/nation.csv' WITH (FORMAT csv, DELIMITER '|');
COPY partsupp FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/partsupp.csv' WITH (FORMAT csv, DELIMITER '|');
COPY lineitem FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/lineitem.csv' WITH (FORMAT csv, DELIMITER '|');
COPY orders FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/orders.csv' WITH (FORMAT csv, DELIMITER '|');
COPY part FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/part.csv' WITH (FORMAT csv, DELIMITER '|');
COPY supplier FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/supplier.csv' WITH (FORMAT csv, DELIMITER '|');
COPY region FROM '/export/scratch2/btang/postgresql-9.6rc1/pdivergen/region.csv' WITH (FORMAT csv, DELIMITER '|');
