import real_power


def SeasonFinder(current_week):
    if (1 <= current_week <= 8) or (44 <= current_week <= 52):
        return "Winter"

    elif (9 <= week_count <= 17) or (31 <= week_count <= 43):
        return "Spring/Fall"

    elif 18 <= week_count <= 30:
        return "Summer"


data_dict = {}

load_feeders = real_power.annual_peak_demand_load_load_feeders
weekly_load_factors = real_power.weekly_load_factors
daily_load_factors = real_power.daily_load_factors
winter_weekday_hourly_load_factors = real_power.hourly_load_factors_weekday_1_8__44_52
winter_weekend_hourly_load_factors = real_power.hourly_load_factors_weekend_1_8__44_52
summer_weekday_hourly_load_factors = real_power.hourly_load_factors_weekday_18_30
summer_weekend_hourly_load_factors = real_power.hourly_load_factors_weekend_18_30
spring_weekday_hourly_load_factors = real_power.hourly_load_factors_weekday_9_17__31_43
spring_weekend_hourly_load_factors = real_power.hourly_load_factors_weekend_9_17__31_43

num_regions = 1
num_aggregators = 1
num_neighborhoods = 1
num_houses = 1

year = 2018
season = "Winter"
power_system = "Sweden"

feed_count = 0
week_count = 0
day_count = 0
hour_count = 0

for feed in load_feeders:
    feed_count = feed_count + 1
    week_count = 0
    data_dict[feed_count] = {}
    # print(f'load_feeders: {feed_count}, {feed}')
    for week in weekly_load_factors:
        week_count = week_count + 1
        day_count = 0
        data_dict[feed_count][week_count] = {}
        # print(f'Week: {week_count}, {week}')
        for day in daily_load_factors:
            day_count = day_count + 1
            data_dict[feed_count][week_count][day_count] = {}
            # print(f'Day: {day_count}, {day}')
            hour_count = 0
            if (week_count >= 1 and week_count <= 8) or (week_count >= 44 and week_count <= 52):
                if day_count == 5 or day_count == 6:
                    for hour in winter_weekend_hourly_load_factors:
                        hour_count = hour_count + 1
                        data_dict[feed_count][week_count][day_count][hour_count] = {}
                        # print(f'Hour: {hour_count}, {hour}')
                        # print(f'AP: {load_feeders[feed][0]}')
                        # print(f'RP: {load_feeders[feed][1]}')
                        # print(f'APP: {load_feeders[feed][2]}')
                        active_power = week * day * hour * load_feeders[feed][0]
                        reactive_power = week * day * hour * load_feeders[feed][1]
                        apparent_power = week * day * hour * load_feeders[feed][2]
                        data_dict[feed_count][week_count][day_count][hour_count] = [active_power, reactive_power,
                                                                                    apparent_power, feed, 0]
                        # print(f'data_dict: {data_dict}')
                        # input()
                else:
                    for hour in winter_weekday_hourly_load_factors:
                        hour_count = hour_count + 1
                        # print(f'Hour: {hour_count}, {hour}')
                        # print(f'AP: {load_feeders[feed][0]}')
                        # print(f'RP: {load_feeders[feed][1]}')
                        # print(f'APP: {load_feeders[feed][2]}')
                        active_power = week * day * hour * load_feeders[feed][0]
                        reactive_power = week * day * hour * load_feeders[feed][1]
                        apparent_power = week * day * hour * load_feeders[feed][2]
                        data_dict[feed_count][week_count][day_count][hour_count] = [active_power, reactive_power,
                                                                                    apparent_power, feed, 0]
                        # print(f'data_dict: {data_dict}')
                        # input()

            elif (week_count >= 9 and week_count <= 17) or (week_count >= 31 and week_count <= 43):
                if day_count == 5 or day_count == 6:
                    for hour in spring_weekend_hourly_load_factors:
                        hour_count = hour_count + 1
                        # print(f'Hour: {hour_count}, {hour}')
                        # print(f'AP: {load_feeders[feed][0]}')
                        # print(f'RP: {load_feeders[feed][1]}')
                        # print(f'APP: {load_feeders[feed][2]}')
                        active_power = week * day * hour * load_feeders[feed][0]
                        reactive_power = week * day * hour * load_feeders[feed][1]
                        apparent_power = week * day * hour * load_feeders[feed][2]
                        data_dict[feed_count][week_count][day_count][hour_count] = [active_power, reactive_power,
                                                                                    apparent_power, feed, 0]
                        # print(f'data_dict: {data_dict}')
                        # input()
                else:
                    for hour in spring_weekday_hourly_load_factors:
                        hour_count = hour_count + 1
                        # print(f'Hour: {hour_count}, {hour}')
                        # print(f'AP: {load_feeders[feed][0]}')
                        # print(f'RP: {load_feeders[feed][1]}')
                        # print(f'APP: {load_feeders[feed][2]}')
                        active_power = week * day * hour * load_feeders[feed][0]
                        reactive_power = week * day * hour * load_feeders[feed][1]
                        apparent_power = week * day * hour * load_feeders[feed][2]
                        data_dict[feed_count][week_count][day_count][hour_count] = [active_power, reactive_power,
                                                                                    apparent_power, feed, 0]
                        # print(f'data_dict: {data_dict}')
                        # input()
            elif (week_count >= 18 and week_count <= 30):
                if day_count == 5 or day_count == 6:
                    for hour in summer_weekend_hourly_load_factors:
                        hour_count = hour_count + 1
                        # print(f'Hour: {hour_count}, {hour}')
                        # print(f'AP: {load_feeders[feed][0]}')
                        # print(f'RP: {load_feeders[feed][1]}')
                        # print(f'APP: {load_feeders[feed][2]}')
                        active_power = week * day * hour * load_feeders[feed][0]
                        reactive_power = week * day * hour * load_feeders[feed][1]
                        apparent_power = week * day * hour * load_feeders[feed][2]
                        data_dict[feed_count][week_count][day_count][hour_count] = [active_power, reactive_power,
                                                                                    apparent_power, feed, 0]
                        # print(f'data_dict: {data_dict}')
                        # input()
                else:
                    for hour in summer_weekday_hourly_load_factors:
                        hour_count = hour_count + 1
                        # print(f'Hour: {hour_count}, {hour}')
                        # print(f'AP: {load_feeders[feed][0]}')
                        # print(f'RP: {load_feeders[feed][1]}')
                        # print(f'APP: {load_feeders[feed][2]}')
                        active_power = week * day * hour * load_feeders[feed][0]
                        reactive_power = week * day * hour * load_feeders[feed][1]
                        apparent_power = week * day * hour * load_feeders[feed][2]
                        data_dict[feed_count][week_count][day_count][hour_count] = [active_power, reactive_power,
                                                                                    apparent_power, feed, 0]
                        # print(f'data_dict: {data_dict}')
                        # input()
# print(feed_count)
