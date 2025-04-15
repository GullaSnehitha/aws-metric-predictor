from app import aws_utils

def test_list_regions():
    regions = aws_utils.list_regions()
    assert isinstance(regions, list)

def test_list_instances():
    region = aws_utils.list_regions()[0]
    instances = aws_utils.list_instances(region)
    assert isinstance(instances, list)
