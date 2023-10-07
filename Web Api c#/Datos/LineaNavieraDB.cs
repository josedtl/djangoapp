using Datos.Conexion;
using System.Data.SqlClient;
using Entidades;
using System.Data;


namespace Datos
{
    public class LineaNavieraDB
    {
        public List<LineaNavieraEntity> GetLineaNaviera()
        {
            List<LineaNavieraEntity> ListaData = new List<LineaNavieraEntity>();

            DatabaseManager dbManager = new DatabaseManager();

            SqlDataReader reader = dbManager.StoreConsulta("sp_LineaNaviera_SelectAll");

            LineaNavieraEntity Item = null;
            while (reader.Read())
            {
                Item = null;
                Item = new LineaNavieraEntity();

                Item.LineaNavieraId = Convert.ToInt32(reader["LineaNavieraId"]);
                Item.Nombre = reader["Nombre"].ToString();
                Item.Color = reader["Color"].ToString();
                Item.Codigo = reader["Codigo"].ToString();
                Item.CodUsuario = reader["CodUsuario"].ToString();
                Item.FechaRegistro = Convert.ToDateTime(reader["FechaRegistro"]);
                Item.EstadoRegistro = Convert.ToBoolean(reader["EstadoRegistro"]);

                ListaData.Add(Item);
            }

            reader.Close();

            return ListaData;
        }
        public List<LineaNavieraEntity> GetLineaNavieraItem(Int32 LineaNavieraId)
        {
            List<LineaNavieraEntity> ListaData = new List<LineaNavieraEntity>();

            DatabaseManager dbManager = new DatabaseManager();


            SqlParameter[] parametros = new SqlParameter[]
       {
            new SqlParameter("@LineaNavieraId", LineaNavieraId)
       };

            SqlDataReader reader = dbManager.StoreConsulta("sp_LineaNaviera_SelectItem", parametros);

            LineaNavieraEntity Item = null;
            while (reader.Read())
            {
                Item = null;
                Item = new LineaNavieraEntity();

                Item.LineaNavieraId = Convert.ToInt32(reader["LineaNavieraId"]);
                Item.Nombre = reader["Nombre"].ToString();
                Item.Color = reader["Color"].ToString();
                Item.Codigo = reader["Codigo"].ToString();
                Item.CodUsuario = reader["CodUsuario"].ToString();
                Item.FechaRegistro = Convert.ToDateTime(reader["FechaRegistro"]);
                Item.EstadoRegistro = Convert.ToBoolean(reader["EstadoRegistro"]);

                ListaData.Add(Item);
            }

            reader.Close();

            return ListaData;
        }

        public LineaNavieraEntity Save(LineaNavieraEntity Ent)
        {
            DatabaseManager dbManager = new DatabaseManager();

            String NameStore = "sp_LineaNaviera_Save";
            if (Ent.LineaNavieraId > 0) NameStore = "sp_LineaNaviera_Update";


            SqlParameter[] parametros = new SqlParameter[]
            {
            new SqlParameter("@LineaNavieraId", Ent.LineaNavieraId)
            {
                Direction= ParameterDirection.InputOutput,
                SqlDbType= SqlDbType.Int
            },
            new SqlParameter("@Nombre", Ent.Nombre),
            new SqlParameter("@Color", Ent.Color),
            new SqlParameter("@Codigo", Ent.Codigo),
            new SqlParameter("@CodUsuario",Ent.CodUsuario),
            new SqlParameter("@FechaRegistro", Ent.FechaRegistro),
            new SqlParameter("@EstadoRegistro", Ent.EstadoRegistro),
            };


            Ent.LineaNavieraId = dbManager.ProcedimientoSave(NameStore, parametros, "@LineaNavieraId");


            return Ent;

        }



        public Boolean Delete(Int32 LineaNavieraId)
        {
            DatabaseManager dbManager = new DatabaseManager();

            SqlParameter[] parametros = new SqlParameter[]
            {
            new SqlParameter("@LineaNavieraId", LineaNavieraId)
            };

            String Store = "sp_LineaNaviera_Delete";
            Boolean Fla = dbManager.ProcedimientoDelete(Store, parametros);

            return Fla;

        }


    }
}
