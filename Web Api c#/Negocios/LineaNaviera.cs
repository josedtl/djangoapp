using System.Data;
using Entidades;
using Datos;

namespace Negocios
{
    public class LineaNaviera
    {
        
            public List<LineaNavieraEntity> GetLineaNaviera()
            {
                LineaNavieraDB DB = new LineaNavieraDB();
                return DB.GetLineaNaviera();
            }

            public List<LineaNavieraEntity> GetLineaNavieraItem(Int32 LineaNavieraId)
            {
                LineaNavieraDB DB = new LineaNavieraDB();
                return DB.GetLineaNavieraItem(LineaNavieraId);
            }

            public LineaNavieraEntity Save(LineaNavieraEntity Ent)
            {
                LineaNavieraDB DB = new LineaNavieraDB();
                return DB.Save(Ent);

            }

            public Boolean Delete(Int32 LineaNavieraId)
            {
                LineaNavieraDB DB = new LineaNavieraDB();
                return DB.Delete(LineaNavieraId);
            }




        
    }
}
