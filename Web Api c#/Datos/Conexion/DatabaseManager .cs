using System.Data;
using System.Data.SqlClient;

namespace Datos.Conexion
{
    public class DatabaseManager : IDisposable
    {


        //192.168.18.14
        private readonly SqlConnection _connection;
        private string connectionString = "Data Source=localhost,14333;Initial Catalog=AlmacenDB;User ID=SA;Password=Admin123;";
        public DatabaseManager()
        {
            _connection = new SqlConnection(connectionString);
        }

        public void OpenConnection()
        {
            if (_connection.State != ConnectionState.Open)
            {
                _connection.Open();
            }
        }

        public SqlDataReader ExecuteQuery(string sqlQuery)
        {
            SqlCommand command = new SqlCommand(sqlQuery, _connection);
            return command.ExecuteReader();
        }

        public void CloseConnection()
        {
            if (_connection.State == ConnectionState.Open)
            {
                _connection.Close();
            }
        }

        public void Dispose()
        {
            _connection.Dispose();
        }

        public int store(string nombreProcedimiento, string parametroCadena, int parametroEntero)
        {
            using (SqlConnection connection = new SqlConnection(connectionString))
            {
                connection.Open();

                using (SqlCommand cmd = new SqlCommand(nombreProcedimiento, connection))
                {
                    cmd.CommandType = CommandType.StoredProcedure;

                    // Parámetro de cadena de entrada
                    SqlParameter paramCadena = new SqlParameter("@ParametroCadena", SqlDbType.VarChar);
                    paramCadena.Value = parametroCadena;
                    cmd.Parameters.Add(paramCadena);

                    // Parámetro entero de entrada
                    SqlParameter paramEntero = new SqlParameter("@ParametroEntero", SqlDbType.Int);
                    paramEntero.Value = parametroEntero;
                    cmd.Parameters.Add(paramEntero);

                    // Parámetro de salida
                    SqlParameter paramSalida = new SqlParameter("@Resultado", SqlDbType.Int);
                    paramSalida.Direction = ParameterDirection.Output;
                    cmd.Parameters.Add(paramSalida);

                    // Ejecuta el procedimiento almacenado
                    cmd.ExecuteNonQuery();

                    // Recupera el valor del parámetro de salida
                    int resultado = (int)paramSalida.Value;

                    return resultado;
                }
            }
        }
        public SqlDataReader StoreConsulta(string nombreProcedimiento, SqlParameter[] parametros = null)
        {
            SqlConnection connection = new SqlConnection(connectionString);
            SqlCommand cmd = null;
            SqlDataReader reader = null;

            try
            {
                connection.Open();
                cmd = new SqlCommand(nombreProcedimiento, connection);
                cmd.CommandType = CommandType.StoredProcedure;

                if (parametros != null)
                {
                    cmd.Parameters.AddRange(parametros);
                }

                reader = cmd.ExecuteReader(CommandBehavior.CloseConnection);

                return reader;
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }


        public Int32 ProcedimientoSave(string nombreProcedimiento, SqlParameter[] parametros, String Devolver)
        {
            SqlConnection connection = new SqlConnection(connectionString);
            SqlCommand cmd = null;

            try
            {
                connection.Open();
                cmd = new SqlCommand(nombreProcedimiento, connection);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddRange(parametros);
                cmd.ExecuteNonQuery();
                object valor = cmd.Parameters[Devolver].Value;
                int idNuevo = 0;
                if (valor != DBNull.Value)
                {
                    idNuevo = Convert.ToInt32(valor);
                }
                return idNuevo;
            }
            catch (Exception ex)
            {
                throw ex;
            }
            finally
            {
                connection.Close();
            }
        }

        public Boolean ProcedimientoDelete(string nombreProcedimiento, SqlParameter[] parametros)
        {
            Boolean fla = false;
            SqlConnection connection = new SqlConnection(connectionString);
            SqlCommand cmd = null;

            try
            {
                connection.Open();
                cmd = new SqlCommand(nombreProcedimiento, connection);
                cmd.CommandType = CommandType.StoredProcedure;
                cmd.Parameters.AddRange(parametros);
                int value = cmd.ExecuteNonQuery();

                if (value == 1) fla = true;
                return fla;
            }
            catch (Exception ex)
            {
                throw ex;
            }
            finally
            {
                connection.Close();
            }
        }
    }
}
