using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DonationService.Models.Entities
{
    public enum Sex
    {
        Male,Female,Other
    }
    public class ChildGroup
    {
        public int Age { get; set; }
        public Sex Sex { get; set; }

        public override string? ToString()
        {
            return $"{Age}";
        }
    }
}
