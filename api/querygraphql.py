class queryGraphql:
     
      def __init__(self ):
      
           self.query_01 ="""{
              allOpportunityApplication 
            
              {
                  paging {
                  total_pages
                }
                data {
                  id
                  status
                  created_at
                  current_status
                  date_approved
                  
                }
                }
            }
              """      
      def chamaGraphQL(self):
              input_query = self.query_01 
              return  input_query
pass