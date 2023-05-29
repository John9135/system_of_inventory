from sqlalchemy import Column, Integer, String

from config.database import Base



class MovieCast(Base):
    
    __tablename__= "movie_cast"

act_id = Column(Integer , ForeignKey("actor.act_id"))
mov_id = Column(Integer , ForeignKey("movie.id"))
role = Column(String(30))