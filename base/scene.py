from base.entity import Entity

class Scene:
    def __init__(self, manager):
        self.manager = manager
        self.entities = {}
        self.components = {}
        self.systems = []

    def create_entity(self):
        entity = Entity()
        self.entities[entity.id] = entity
        return entity

    def add_component(self, entity, component):
        component_type = type(component)
        if component_type not in self.components:
            self.components[component_type] = {}
        self.components[component_type][entity.id] = component

    def get_component(self, entity, component_type):
        if component_type in self.components:
            return self.components[component_type][entity.id]
        return None
    
    def remove_component(self, entity, component_type):
        if component_type in self.components and entity.id in self.components[component_type]:
            del self.components[component_type][entity.id]

    def delete_entity(self, entity):
        if entity.id not in self.entities:
            return
        del self.entities[entity.id]
        for component_type in self.components:
            if entity.id in self.components[component_type]:
                del self.components[component_type][entity.id]

    def add_system(self, system):
        self.systems.append(system)
        system.scene = self

    def process_systems(self, dt):
        for system in self.systems:
            system.process(dt)

    def get_components_for_entities(self, *component_types):
        if not component_types:
            return
        
        if component_types[0] not in self.components:
            return
        
        candidate_entities_ids = set(self.components[component_types[0]].keys())
        for component_type in component_types[1:]:
            if component_type not in self.components:
                return
            candidate_entities_ids &= set(self.components[component_type].keys())
        
        for entity_id in candidate_entities_ids:
            yield (entity_id,) + tuple(self.components[comp_type][entity_id] for comp_type in component_types)