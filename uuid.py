import uuid


def create_uid():
    """create log id"""
    return ''.join(str(uuid.uuid1()).split('-'))
