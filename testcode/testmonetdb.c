#include <stdio.h>
#include <mapi.h> 
#include <stdlib.h>

int main(int argc, char* argv[])
{
	printf("hello world, MonetDB mapi\n");
 	Mapi dbh; 
	MapiHdl hdl = NULL; 
	dbh = mapi_connect("localhost", 50000, "monetdb", "monetdb", "sql", "tpch"); 
	if (mapi_error(dbh)) 
	{
		printf("connect monetdb server failed");
		if (hdl != NULL) 
		{ 
			mapi_explain_query(hdl, stderr); 
			do { 
				if (mapi_result_error(hdl) != NULL) {
					mapi_explain_result(hdl, stderr); 
				}
			} while (mapi_next_result(hdl) == 1); 
			mapi_close_handle(hdl); 
			mapi_destroy(dbh); 
		} else if (dbh != NULL) { 
			 mapi_explain(dbh, stderr); 
			 mapi_destroy(dbh); 
		} else { 
			 fprintf(stderr, "command failed\n"); 
  		}
		exit(-1); 
	}
	else
	{
		printf("connect monetdb server success\n");
//		mapi_close_handle(hdl); 
		mapi_destroy(dbh); 
	}
	return 0;
}
