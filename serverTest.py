import pymysql
import traceback
import sys
import random
import time

start_time = time.time()


# Define functions

# connect_database connects the program to a database and creates a cursor
def connect_database(host, user, password, database):
    # Attempt connection to the database
    try:
        db = pymysql.connect(host,  # your host, usually localhost
                             user,  # your username
                             password,  # your password
                             database)  # name of the data base
        return db
    except:
        print("############################################################")
        print("There was an error while trying to connect to the database.")
        traceback.print_exc()
        print("############################################################")
        sys.exit()


def create_appliance_type_table(cursor):
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS ApplianceType(
            TYPE_ID CHAR(6), 
            DESCRIPTION TINYTEXT, 
            PRIMARY KEY(TYPE_ID))""")
    except:
        print("############################################################")
        print("The Appliance Type table could not be generated.")
        traceback.print_exc()
        print("############################################################")


def create_appliance_table(cursor):
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Appliance(
            APPLIANCE_ID CHAR(4), 
            HOUSE_ID CHAR(4), 
            NEIGHBORHOOD_ID CHAR(4), 
            AGG_ID CHAR(4), 
            REG_ID CHAR(4), 
            TYPE_ID CHAR(6), 
            APP_CONSUMPTION BIGINT, 
            CONSTRAINT PK_Appliance PRIMARY KEY(APPLIANCE_ID, HOUSE_ID, NEIGHBORHOOD_ID, AGG_ID, REG_ID), 
            FOREIGN KEY (TYPE_ID) REFERENCES ApplianceType(TYPE_ID), 
            FOREIGN KEY (HOUSE_ID) REFERENCES House(HOUSE_ID), 
            FOREIGN KEY (NEIGHBORHOOD_ID) REFERENCES Neighborhood(NEIGHBORHOOD_ID), 
            FOREIGN KEY (AGG_ID) REFERENCES Aggregator(AGG_ID),
            FOREIGN KEY (REG_ID) REFERENCES Region(REG_ID))""")
    except:
        print("############################################################")
        print("The Appliance table could not be generated.")
        traceback.print_exc()
        print("############################################################")


def create_house_table(cursor):
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS House(
            HOUSE_ID CHAR(4), 
            NEIGHBORHOOD_ID CHAR(4), 
            AGG_ID CHAR(4), 
            REG_ID CHAR(4), 
            HOUSE_CONSUMPTION BIGINT, 
            CONSTRAINT PK_House PRIMARY KEY(HOUSE_ID, NEIGHBORHOOD_ID, AGG_ID, REG_ID), 
            FOREIGN KEY(NEIGHBORHOOD_ID) REFERENCES Neighborhood(NEIGHBORHOOD_ID),
            FOREIGN KEY (AGG_ID) REFERENCES Aggregator(AGG_ID),
            FOREIGN KEY (REG_ID) REFERENCES Region(REG_ID))""")
    except:
        print("############################################################")
        print("The House table could not be generated.")
        traceback.print_exc()
        print("############################################################")


def create_readings_table(cursor):
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Readings(
            DATE_TIME CHAR(19), 
            HOUSE_ID CHAR(4), 
            NEIGHBORHOOD_ID CHAR(4), 
            AGG_ID CHAR(4), 
            REG_ID CHAR(4), 
            kWh BIGINT, 
            OUTDOOR_TEMP int(3), 
            CONSTRAINT PK_Reading PRIMARY KEY (DATE_TIME, HOUSE_ID, NEIGHBORHOOD_ID, AGG_ID, REG_ID), 
            FOREIGN KEY(HOUSE_ID) REFERENCES House(HOUSE_ID), 
            FOREIGN KEY(NEIGHBORHOOD_ID) REFERENCES Neighborhood(NEIGHBORHOOD_ID), 
            FOREIGN KEY(AGG_ID) REFERENCES Aggregator(AGG_ID), 
            FOREIGN KEY(REG_ID) REFERENCES Region(REG_ID))""")
    except:
        print("############################################################")
        print("The Readings table could not be generated.")
        traceback.print_exc()
        print("############################################################")


def create_neighborhood_table(cursor):
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Neighborhood(
            NEIGHBORHOOD_ID CHAR(4), 
            AGG_ID CHAR(4), 
            REG_ID CHAR(4), 
            NEIGHBORHOOD_CONSUMPTION BIGINT, 
            CONSTRAINT PK_Neighborhood PRIMARY KEY (NEIGHBORHOOD_ID, AGG_ID, REG_ID), 
            FOREIGN KEY(AGG_ID) REFERENCES Aggregator(AGG_ID), 
            FOREIGN KEY(REG_ID) REFERENCES Region(REG_ID))""")
    except:
        print("############################################################")
        print("The Neighborhood table could not be generated.")
        traceback.print_exc()
        print("############################################################")


def create_aggregator_table(cursor):
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Aggregator(
            AGG_ID CHAR(4), 
            REG_ID CHAR(4), 
            AGG_CONSUMPTION BIGINT, 
            CONSTRAINT PK_Aggregator PRIMARY KEY (AGG_ID, REG_ID), 
            FOREIGN KEY(REG_ID) REFERENCES Region(REG_ID))""")
    except:
        print("############################################################")
        print("The Aggregator table could not be generated.")
        traceback.print_exc()
        print("############################################################")


def create_region_table(cursor):
    try:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS Region(
            REG_ID CHAR(4),
            REG_CONSUMPTION BIGINT, 
            PRIMARY KEY(REG_ID))""")
    except:
        print("############################################################")
        print("The Region table could not be generated.")
        traceback.print_exc()
        print("############################################################")


def drop_table(cursor, table_name):
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    except:
        print("############################################################")
        print(f"The {table_name} table could not be dropped.")
        traceback.print_exc()
        print("############################################################")


def drop_all_tables(cursor):
    try:
        cursor.execute("DROP TABLE IF EXISTS Readings")
        cursor.execute("DROP TABLE IF EXISTS Appliance")
        cursor.execute("DROP TABLE IF EXISTS House")
        cursor.execute("DROP TABLE IF EXISTS Neighborhood")
        cursor.execute("DROP TABLE IF EXISTS Aggregator")
        cursor.execute("DROP TABLE IF EXISTS Region")
        cursor.execute("DROP TABLE IF EXISTS ApplianceType")
    except:
        print("############################################################")
        print("All tables could not be dropped.")
        traceback.print_exc()
        print("############################################################")


def create_all_tables(cursor):
    try:
        create_appliance_type_table(cursor)
        create_region_table(cursor)
        create_aggregator_table(cursor)
        create_neighborhood_table(cursor)
        create_house_table(cursor)
        create_appliance_table(cursor)
        create_readings_table(cursor)
    except:
        print("############################################################")
        print("All tables could not be generated.")
        traceback.print_exc()
        print("############################################################")


def insert_appliance_type(db, cursor, type_id, description):
    try:
        cursor.execute(
            f"INSERT INTO ApplianceType(TYPE_ID, DESCRIPTION) VALUES({type_id}, {description})")
        db.commit()
    except:
        print("############################################################")
        print("ApplianceType could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def remove_appliance_type(db, cursor, type_id, description):
    try:
        cursor.execute(
            f"DELETE FROM ApplianceType WHERE TYPE_ID = {type_id}")
        db.commit()
    except:
        print("############################################################")
        print("ApplianceType could not be deleted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def insert_neighborhood(db, cursor, neighborhood_id, agg_id, reg_id, neighborhood_consumption):
    try:
        cursor.execute(
            f"INSERT INTO Neighborhood(NEIGHBORHOOD_ID, AGG_ID, REG_ID, NEIGHBORHOOD_CONSUMPTION) VALUES({neighborhood_id}, {agg_id}, {reg_id}, {neighborhood_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("Neighborhood could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def remove_neighborhood(db, cursor, neighborhood_id, agg_id, reg_id):
    try:
        cursor.execute(
            f"DELETE FROM Neighborhood WHERE PK_Neighborhood = ({neighborhood_id}, {agg_id}, {reg_id})")
        db.commit()
    except:
        print("############################################################")
        print("Neighborhood could not be deleted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def insert_appliance_with_application_type_description(db, cursor, appliance_id, house_id, description, consumption):
    try:
        cursor.execute(f"SELECT * FROM ApplianceType WHERE DESCRIPTION = {description}")
        temp_appliance_type_variable = cursor.fetchone()
        temp_type_id = f"'{temp_appliance_type_variable[0]}'"
        cursor.execute(
            f"INSERT INTO Appliance(APPLIANCE_ID, HOUSE_ID, CONSUMPTION, TYPE_ID) VALUES({appliance_id}, {house_id}, {consumption}, {temp_type_id})")
        db.commit()
    except:
        print("############################################################")
        print("ApplianceType could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def insert_house(db, cursor, house_id, neighborhood_id, agg_id, reg_id, house_consumption):
    try:
        cursor.execute(
            f"INSERT INTO House(HOUSE_ID, NEIGHBORHOOD_ID, AGG_ID, REG_ID, HOUSE_CONSUMPTION) VALUES({house_id}, {neighborhood_id}, {agg_id}, {reg_id}, {house_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("House could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def remove_house(db, cursor, house_id, neighborhood_id, agg_id, reg_id, house_consumption):
    try:
        cursor.execute(
            f"DELETE FROM House WHERE PK_House = ({house_id}, {neighborhood_id}, {agg_id}, {reg_id}, {house_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("House could not be deleted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def insert_readings(db, cursor, date_time, house_id, neighborhood_id, agg_id, reg_id, kwh, outdoor_temp):
    try:
        cursor.execute(
            f"INSERT INTO Readings(DATE_TIME, HOUSE_ID, NEIGHBORHOOD_ID, AGG_ID, REG_ID, kWh, OUTDOOR_TEMP) VALUES({date_time}, {house_id}, {neighborhood_id}, {agg_id}, {reg_id}, {kwh}, {outdoor_temp})")
        db.commit()
    except:
        print("############################################################")
        print("Reading could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def remove_readings(db, cursor, date_time, house_id, neighborhood_id, agg_id, reg_id, kwh, outdoor_temp):
    try:
        cursor.execute(
            f"DELETE FROM Readings WHERE PK_Reading = ({date_time}, {house_id}, {neighborhood_id}, {agg_id}, {reg_id}, {kwh}, {outdoor_temp})")
        db.commit()
    except:
        print("############################################################")
        print("Reading could not be deleted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def insert_appliance(db, cursor, appliance_id, house_id, neighborhood_id, agg_id, reg_id, type_id, app_consumption):
    try:
        cursor.execute(
            f"INSERT INTO Appliance(APPLIANCE_ID, HOUSE_ID, NEIGHBORHOOD_ID, AGG_ID, REG_ID, TYPE_ID, APP_CONSUMPTION) VALUES({appliance_id}, {house_id}, {neighborhood_id}, {agg_id}, {reg_id}, {type_id}, {app_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("Appliance could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def remove_appliance(db, cursor, appliance_id, house_id, neighborhood_id, agg_id, reg_id, type_id, app_consumption):
    try:
        cursor.execute(
            f"DELETE FROM Appliance WHERE PK_Appliance = ({appliance_id}, {house_id}, {neighborhood_id}, {agg_id}, {reg_id}, {type_id}, {app_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("Appliance could not be deleted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def insert_aggregator(db, cursor, agg_id, reg_id, agg_consumption):
    try:
        cursor.execute(
            f"INSERT INTO Aggregator(AGG_ID, REG_ID, AGG_CONSUMPTION) VALUES({agg_id}, {reg_id}, {agg_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("Aggregator could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def remove_aggregator(db, cursor, agg_id, reg_id, agg_consumption):
    try:
        cursor.execute(
            f"DELETE FROM Aggregator WHERE PK_Aggregator = ({agg_id}, {reg_id}, {agg_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("Aggregator could not be deleted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def insert_region(db, cursor, reg_id, reg_consumption):
    try:
        cursor.execute(
            f"INSERT INTO Region(REG_ID, REG_CONSUMPTION) VALUES({reg_id}, {reg_consumption})")
        db.commit()
    except:
        print("############################################################")
        print("Region could not be inserted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def remove_region(db, cursor, reg_id, agg_id, reg_consumption):
    try:
        cursor.execute(
            f"DELETE FROM Region WHERE REG_ID = {reg_id}")
        db.commit()
    except:
        print("############################################################")
        print("Region could not be deleted.")
        traceback.print_exc()
        print("############################################################")
        db.rollback()


def clear_tables(cursor):
    try:
        drop_all_tables(cursor)
        create_all_tables(cursor)
    except:
        print("############################################################")
        print("All tables could not be deleted.")
        traceback.print_exc()
        print("############################################################")

# The purpose of this function is to delete any data that is currently in the database and fill it with random,
# but correlated, data. Currently the function inserts one year of data (12 months, 30 days per month, 24 hours per day)
def auto_fill_db(db, cursor):

    # Clear all tables/data in the database
    clear_tables(cursor)

    # num_regions = input("Number of regions: ")
    # num_aggregators = input("Number of aggregators: ")
    # num_neighborhoods = input("Number of neighborhoods: ")
    # num_houses = input("Number of houses: ")
    # num_appliance_types = input("Number of appliance types: ")
    # num_appliances = input("Number of appliances: ")

    # num_regions = 1
    # num_aggregators = 1
    # num_neighborhoods = 1
    # num_houses = 1
    # num_appliances = 1
    # num_appliance_types = 1

# Randomly select a number of regions, aggregators, neighborhoods, houses, appliances, and appliance types to fill db
    num_regions = random.randint(1, 3)
    num_aggregators = random.randint(1, 3)
    num_neighborhoods = random.randint(2, 5)
    num_houses = random.randint(3, 10)
    num_appliances = random.randint(1, 10)
    num_appliance_types = random.randint(3, 15)

    print(f"Num regions: {num_regions}")
    print(f"Num agg: {num_aggregators}")
    print(f"Num hoods: {num_neighborhoods}")
    print(f"Num houses: {num_houses}")
    print(f"Num appliances: {num_appliances}")
    print(f"Num app types: {num_appliance_types}")

    # Generate appliance types
    # Each appliance type will have the description "Appliance 'n'" for every nth appliance
    for app_type_index in range(1, num_appliance_types + 1):
        description = f"Appliance {app_type_index}"
        insert_appliance_type(db, cursor, f"'{app_type_index}'", f"'{description}'")

    # Generate Regions and aggregators and neighborhoods and houses and appliances and readings

    # The outer most layer is the region layer. There will be some number of regions between 2 and 20.
    # The regional consumption is based on estimated minimum and maximum power consumption for a region.
    # The consumption min and max is estimated based off of the following:
    #     Power consumption per house: Min = 3 kWh, max = 550,000
    #     Houses per neighborhood: Min = 10, Max = 50
    #     Neighborhoods per aggregator: Min = 3, Max = 50
    #     Aggregators per region: Min = 2, Max = 20
    #     Regions in database: Min = 2, Max = 20
    for reg_index in range(1, num_regions + 1):
        reg_consumption = random.randint(1500000, 250000000000000)

        insert_region(db,
                      cursor,
                      f"'{reg_index}'",
                      f"'{reg_consumption}'"
                      )

        # The next layer is the aggregator layer. There will be some number of aggregators between 2 and 20
        for agg_index in range(1, num_aggregators + 1):
            agg_consumption = random.randint(750000, 12500000000000)
            reg_consumption = reg_consumption - agg_consumption

            if agg_index == num_aggregators:
                agg_consumption = agg_consumption + reg_consumption

            insert_aggregator(db,
                              cursor,
                              f"'{agg_index}'",
                              f"'{reg_index}'",
                              f"'{agg_consumption}'"
                              )

            for neighborhood_index in range(1, num_neighborhoods + 1):
                neighborhood_consumption = random.randint(250000, 250000000000)
                agg_consumption = agg_consumption - neighborhood_consumption

                if neighborhood_index == num_neighborhoods:
                    neighborhood_consumption = neighborhood_consumption + agg_consumption

                insert_neighborhood(db,
                                    cursor,
                                    f"'{neighborhood_index}'",
                                    f"'{agg_index}'",
                                    f"'{reg_index}'",
                                    f"'{neighborhood_consumption}'"
                                    )

                for house_index in range(1, num_houses + 1):
                    house_consumption = random.randint(26000, 5000000000)
                    house_consumption2 = house_consumption
                    neighborhood_consumption = neighborhood_consumption - house_consumption

                    if house_index == num_houses:
                        house_consumption = house_consumption + neighborhood_consumption

                    insert_house(db,
                                 cursor,
                                 f"'{house_index}'",
                                 f"'{neighborhood_index}'",
                                 f"'{agg_index}'",
                                 f"'{reg_index}'",
                                 f"'{house_consumption}'")

                    for appliance_index in range(1, num_appliances + 1):
                        appliance_consumption = random.randint(3, 5000000000)
                        house_consumption = house_consumption - appliance_consumption
                        app_type_id = random.randint(1, num_appliance_types)

                        if appliance_index == num_appliances:
                            appliance_consumption = appliance_consumption + house_consumption

                        insert_appliance(db,
                                         cursor,
                                         f"'{appliance_index}'",
                                         f"'{house_index}'",
                                         f"'{neighborhood_index}'",
                                         f"'{agg_index}'",
                                         f"'{reg_index}'",
                                         f"'{app_type_id}'",
                                         f"'{appliance_consumption}'"
                                         )

                    for readings_months in range(1, 13):

                        if readings_months == 1 or readings_months == 2 or readings_months == 3:
                            min_temp = 0
                            max_temp = 30
                        elif readings_months == 4 or readings_months == 5 or readings_months == 6:
                            min_temp = 30
                            max_temp = 70
                        elif readings_months == 7 or readings_months == 8 or readings_months == 9:
                            min_temp = 70
                            max_temp = 100
                        else:
                            min_temp = 30
                            max_temp = 70

                        for readings_days in range(1, 31):
                            outdoor_temp = random.randint(min_temp, max_temp)

                            for readings_hours in range(1, 25):
                                temp_fluctuation = random.randint(0, 6)
                                outdoor_temp = outdoor_temp + temp_fluctuation
                                kwh = random.randint(3, 550000) + ((100 * outdoor_temp) * random.randint(-1, 1))
                                house_consumption2 = house_consumption2 - kwh

                                if readings_months == 12 and readings_days == 7 and readings_hours == 24:
                                    kwh = kwh + house_consumption2

                                insert_readings(db,
                                                cursor, 
                                                f"'{readings_hours}:00:00 {readings_days}-{readings_months}-2018'", 
                                                f"'{house_index}'", 
                                                f"'{neighborhood_index}'",
                                                f"'{agg_index}'", 
                                                f"'{reg_index}'",
                                                f"'{kwh}'", 
                                                f"'{outdoor_temp}'")


def retrieve_appliance_types(cursor):
    try:
        cursor.execute("SELECT * FROM ApplianceType")
        results = cursor.fetchall()
        for row in results:
            appliance_type = row[
            description = row[1]
            print("Appliance Type: {appliance_type}".format(appliance_type=appliance_type))
            print("Description: {description}".format(description=description))
    except:
        print("############################################################")
        print("Appliance types could not be retrieved.")
        traceback.print_exc()
        print("############################################################")


def retrieve_neighborhoods(cursor):
    try:
        cursor.execute("SELECT * FROM Neighborhood")
        results = cursor.fetchall()
        for row in results:
            neighborhood_id = row[0]
            agg_id = row[1]
            print("Neighborhood ID: {neighborhood_ID}".format(neighborhood_ID=neighborhood_id))
            print("Agg ID: {agg_id}".format(agg_id=agg_id))
    except:
        print("############################################################")
        print("Neighborhoods could not be retrieved.")
        traceback.print_exc()
        print("############################################################")


def retrieve_houses(cursor):
    try:
        cursor.execute("SELECT * FROM House")
        results = cursor.fetchall()
        for row in results:
            house_id = row[0]
            neighborhood_id = row[1]
            house_consumption = row[2]
            print("House ID: {house_id}".format(house_id=house_id))
            print("Neighborhood ID: {neighborhood_id}".format(neighborhood_id=neighborhood_id))
            print("House Consumption: {house_consumption}".format(house_consumption=house_consumption))
    except:
        print("############################################################")
        print("Houses could not be retrieved.")
        traceback.print_exc()
        print("############################################################")


def retrieve_readings(cursor):
    try:
        cursor.execute("SELECT * FROM Reading")
        results = cursor.fetchall()
        for row in results:
            date_time = row[0]
            house_id = row[1]
            kWh = row[2]
            outdoor_temp = row[3]
            print("Dates and times: {date_time}".format(date_time=date_time))
            print("House Id's: {house_id}".format(house_id=house_id))
            print("Kilowatt hours: {kWh}".format(kWh=kWh))
            print("Outdoor temperatures: {outdoor_temp}".format(outdoor_temp=outdoor_temp))
    except:
        print("############################################################")
        print("Readings could not be retrieved.")
        traceback.print_exc()
        print("############################################################")


def retrieve_appliances(cursor):
    try:
        cursor.execute("SELECT * FROM Appliance")
        results = cursor.fetchall()
        for row in results:
            appliance_id = row[0]
            house_id = row[1]
            type_id = row[2]
            app_consumption = row[3]
            print("Appliance ID: {appliance_id}".format(appliance_id=appliance_id))
            print("House ID: {house_id}".format(house_id=house_id))
            print("Type ID: {type_id}".format(type_id=type_id))
            print("Appliance Consumption: {app_consumption}".format(app_consumption=app_consumption))
    except:
        print("############################################################")
        print("Appliances could not be retrieved.")
        traceback.print_exc()
        print("############################################################")


##### Connect to database #####

db = connect_database("localhost", "root", "smartgridserver", "pythonbase")
cursor = db.cursor()

##### Create tables #####
# create_appliance_type_table(cursor)
# create_neighborhood_table(cursor)
# create_house_table(cursor)
# create_appliance_table(cursor)
# create_readings_table(cursor)

# create_all_tables(cursor)

##### Drop tables #####
# drop_table(cursor, "Appliance")
# drop_all_tables(cursor)

##### Insert data #####
# insert_appliance_type(db, cursor, "'01'", "'COFFEE-MAKER'")
# insert_neighborhood(db, cursor, "'001'")
# insert_house(db, cursor, "'0011'", "'001'")
# insert_appliance(db, cursor, "'01'", "'0011'", "'175'", "'01'")
# insert_appliance_with_application_type_description(db, cursor, "'01'", "'0011'", "175", "'COFFEE-MAKER'")
# insert_readings(db, cursor, "'2018-06-01 08:00:00'", "'0011'", "'175'", "'75'")

##### Retreive data #####
# retrieve_appliance_type(cursor)
# retrieve_neighborhood(cursor)
# retrieve_house(cursor)
# retrieve_reading(cursor)
# retrieve_appliance(cursor)

##### Remove data #####
# remove_readings(db, cursor, "'2018-06-01 08:00:00'", "'0011'", "'175'", "'75'")
# remove_appliance(db, cursor, "'01'", "'0011'", "'175'", "'01'")
# remove_house(db, cursor, "'0011'", "'001'")
# remove_neighborhood(db, cursor, "'001'")
# remove_applianceType(db, cursor, "'01'", "'COFFEE-MAKER'")
# clear_tables(cursor)

##### auto_fill_db #####
auto_fill_db(db, cursor)

db.close()

print("My program took", time.time() - start_time, "to run")
