from models.mesa import Mesa
from repositorios.repositorio_mesa import InterfaceRepository

class controlador_mesa:
  def __init__(self):
    self.repo = InterfaceRepository()

  #Listar
  def index(self):
    return self.repo.find_all()

  #Crear
  def create(self, info_mesa):
    nueva_mesa = Mesa(info_mesa)
    return self.repo.save(nueva_mesa)

  #Leer
  def show(self, id):
    return self.repo.find_by_id(id)

  #Actualizar
  def update(self, id, info_mesa):
    mesa_actualizada = Mesa(info_mesa)
    return self.repo.update(id, mesa_actualizada)

  #delete
  def delete(self, id):
    return self.repo.delete(id)