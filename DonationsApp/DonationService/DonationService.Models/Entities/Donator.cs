using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DonationService.Models.Entities
{
    public class Donator
    {
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string HomeAddress { get; set; }

        public override string? ToString()
        {
            return $"FirstName: {FirstName}, LastName: {LastName}, HomeAddress: {HomeAddress}";
        }
    }
}
