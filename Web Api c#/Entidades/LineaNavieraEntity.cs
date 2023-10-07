

namespace Entidades
{
    public class LineaNavieraEntity
    {
        public LineaNavieraEntity() {
            this.Item = 0;
            this.LineaNavieraId = 0;
            this.Nombre = String.Empty;
            this.Color = String.Empty;
            this.Codigo = String.Empty;
            this.CodUsuario = String.Empty;
            this.FechaRegistro = DateTime.Now;
            this.EstadoRegistro = false;

        }

        public Int32 Item { get; set; }
        public Int32 LineaNavieraId { get; set; }
        public String Nombre { get; set; }
        public String Color { get; set; }
        public String Codigo { get; set; }
        public String CodUsuario { get; set; }
        public DateTime FechaRegistro { get; set; }
        public Boolean EstadoRegistro { get; set; }

    }
}
