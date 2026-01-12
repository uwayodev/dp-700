[StagingDefinition = [Kind = "FastCopy"]]
section Section1;
shared #"departments csv" = let
  Source = Lakehouse.Contents([HierarchicalNavigation = null]),
  #"Navigation 1" = Source{[workspaceId = "3e2204cc-b967-485c-bf55-8dfa0134abad"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[lakehouseId = "d1e02103-b302-434c-989c-0c63e9f193e1"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 4" = #"Navigation 3"{[Name = "dp700_e008"]}[Content],
  #"Navigation 5" = #"Navigation 4"{[Name = "departments.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 5", [Delimiter = ",", Columns = 4, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"department_id", Int64.Type}, {"department_name", type text}, {"manager", type text}, {"location", type text}})
in
  #"Changed column type";
shared #"employees csv" = let
  Source = Lakehouse.Contents([HierarchicalNavigation = null]),
  #"Navigation 1" = Source{[workspaceId = "3e2204cc-b967-485c-bf55-8dfa0134abad"]}[Data],
  #"Navigation 2" = #"Navigation 1"{[lakehouseId = "d1e02103-b302-434c-989c-0c63e9f193e1"]}[Data],
  #"Navigation 3" = #"Navigation 2"{[Id = "Files", ItemKind = "Folder"]}[Data],
  #"Navigation 4" = #"Navigation 3"{[Name = "dp700_e008"]}[Content],
  #"Navigation 5" = #"Navigation 4"{[Name = "employees.csv"]}[Content],
  #"Imported CSV" = Csv.Document(#"Navigation 5", [Delimiter = ",", Columns = 5, QuoteStyle = QuoteStyle.None]),
  #"Promoted headers" = Table.PromoteHeaders(#"Imported CSV", [PromoteAllScalars = true]),
  #"Changed column type" = Table.TransformColumnTypes(#"Promoted headers", {{"employee_id", Int64.Type}, {"name", type text}, {"department_id", Int64.Type}, {"hire_date", type date}, {"salary", Int64.Type}})
in
  #"Changed column type";
[DataDestinations = {[Definition = [Kind = "Reference", QueryName = "Merge_DataDestination", IsNewTarget = true], Settings = [Kind = "Automatic", TypeSettings = [Kind = "Table"]]]}]
shared Merge = let
  Source = Table.NestedJoin(#"employees csv", {"department_id"}, #"departments csv", {"department_id"}, "departments csv", JoinKind.LeftOuter),
  #"Expanded departments csv" = Table.ExpandTableColumn(Source, "departments csv", {"department_id", "department_name", "manager", "location"}, {"department_id.1", "department_name", "manager", "location"}),
  #"Split column by delimiter" = Table.SplitColumn(#"Expanded departments csv", "name", Splitter.SplitTextByDelimiter(" "), {"name.1", "name.2"}),
  #"Renamed columns" = Table.RenameColumns(#"Split column by delimiter", {{"name.1", "first_name"}, {"name.2", "last_name"}}),
  #"Choose columns" = Table.SelectColumns(#"Renamed columns", {"employee_id", "first_name", "last_name", "department_name", "location"})
in
  #"Choose columns";
shared Merge_DataDestination = let
  Pattern = Lakehouse.Contents([HierarchicalNavigation = null, CreateNavigationProperties = false, EnableFolding = false]),
  Navigation_1 = Pattern{[workspaceId = "3e2204cc-b967-485c-bf55-8dfa0134abad"]}[Data],
  Navigation_2 = Navigation_1{[lakehouseId = "d1e02103-b302-434c-989c-0c63e9f193e1"]}[Data],
  TableNavigation = Navigation_2{[Id = "dp700_e008_person_df2", ItemKind = "Table"]}?[Data]?
in
  TableNavigation;
