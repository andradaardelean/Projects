using LocationService.Models.Entities;

namespace LocationService.Models.Requests
{
    public class AddCenterRequest
    {
        public string State { get; set; }
        public string City { get; set; }
        public string Name { get; set; }
        public string Address { get; set; }
    }
}
