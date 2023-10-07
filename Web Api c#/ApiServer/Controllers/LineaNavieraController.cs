using Microsoft.AspNetCore.Mvc;
using Entidades;
using Negocios;

namespace ApiServer.Controllers
{

    [Route("api/[controller]")]
    [ApiController]
    public class LineaNavieraController : ControllerBase
    {

        [HttpGet]
        [Route("GetAll")]
        public List<LineaNavieraEntity> GetAll()
        {
            try
            {
                LineaNaviera NG = new LineaNaviera();
                var Items = NG.GetLineaNaviera();
                return Items;

            }
            catch (Exception ex)
            {
                return null;
            }
        }

        [HttpGet]
        [Route("Gettem/{LineaNavieraId}")]
        public List<LineaNavieraEntity> Gettem(Int32 LineaNavieraId)
        {
            try
            {
                LineaNaviera NG = new LineaNaviera();
                var Items = NG.GetLineaNavieraItem(LineaNavieraId);
                return Items;

            }
            catch (Exception ex)
            {
                return null;
            }
        }

        [HttpPost]
        [Route("Save")]
        public LineaNavieraEntity Save(LineaNavieraEntity Ent)
        {
            try
            {
                LineaNaviera NG = new LineaNaviera();
                var Items = NG.Save(Ent);
                return Items;

            }
            catch (Exception ex)
            {
                return null;
            }
        }

        [HttpDelete]
        [Route("Delete/{LineaNavieraId}")]
        public Boolean Delete(Int32 LineaNavieraId)
        {
            try
            {
                LineaNaviera NG = new LineaNaviera();
                var Fla = NG.Delete(LineaNavieraId);
                return Fla;

            }
            catch (Exception ex)
            {
                return false;
            }
        }

        [HttpGet]
        [Route("GetAllAlter")]
        public List<LineaNavieraEntity> GetAllAlter()
        {
            try
            {
                LineaNaviera NG = new LineaNaviera();
                var Items = NG.GetLineaNaviera();
                return Items;

            }
            catch (Exception ex)
            {
                return null;
            }
        }

    }
}
