from autofixture import AutoFixture
from dash.models import Region, Aggregator, Neighborhood, House

fixture = AutoFixture(Region)
entries = fixture.create(10)

fixture = AutoFixture(Aggregator)
entries = fixture.create(10)

fixture = AutoFixture(Neighborhood)
entries = fixture.create(10)

fixture = AutoFixture(House)
entries = fixture.create(10)

fixture = AutoFixture(Aggregator, field_values={
    'aggregator_id': generators.InstanceSelector(
        Region,
        limit_choices_to={'region_id':"Labore"})
})
