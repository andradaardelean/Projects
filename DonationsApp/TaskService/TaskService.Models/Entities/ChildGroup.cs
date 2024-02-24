namespace TaskService.Models.Entities
{
    public enum Sex
    {
        Male, Female, Other
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
