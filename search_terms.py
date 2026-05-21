from enums import Category

interventions = {
    
    Category.dbt: ["DBT", "dialectical behavior therapy"],
    Category.act: ["ACT", "acceptance and commitment therapy"],

}

outcomes = {

    Category.depression: ["depression", "depressive", "depressive disorder", "MDD", "PDD"],
    Category.anxiety: ["anxiety", "anxious", "anxiety disorder", "panic", "phobia", "GAD"],
    Category.self_injury: ["self-injury", "self injury", "self-harm", "self harm", "NSSI"]

}

populations = {

    Category.lgbt: ["LGBT", "LGBTQ", "LGBTQ+", "LGBTQIA", "LGBTQIA+", "queer", "gay", "lesbian", "bisexual", "transgender", "genderqueer", "non binary", "non-binary", "nonbinary"],
    Category.undocumented: ["undocumented", "immigrant", "migrant", "emigrant", "DACA", "unauthorized", "illegal"],
    Category.children: ["children", "youth", "kids", "students", "young people"],

}