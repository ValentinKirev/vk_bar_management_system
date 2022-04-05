def dumper(entity):
    return entity.to_json()


def object_hook(jsdict):
    entity_module_name = jsdict['_module']
    entity_class_name = jsdict['_class']
    module = __import__(entity_module_name, fromlist=[entity_class_name])
    cls = getattr(module, entity_class_name)
    return cls.from_json(jsdict)
