namespace TaskService.Models.Entities
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

