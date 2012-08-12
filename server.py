import SocketServer,urllib,httplib,gzip,StringIO

def decode_gzip(compresseddata):
    	compressedstream = StringIO.StringIO(compresseddata)
    	gzipper = gzip.GzipFile(fileobj = compressedstream)
    	return gzipper.read()	
def craft_res(code,reason,ver,res_head,res_body):
	if ver == 10:
		http_ver = "HTTP/1.0"
	if ver == 11:
		http_ver = "HTTP/1.1"
	head_buff = ''
	for i in range(0,len(res_head)):
        	e1 =  res_head[i]
		if e1[1] == "gzip":
			res_body = decode_gzip(res_body)
        	head_buff += e1[0]+": "+e1[1]+"\r\n"
	head_buff = head_buff.replace('\r\ncontent-encoding: gzip','')
	final_res = http_ver+" "+str(code)+" "+reason+"\r\n"+head_buff+"\r\n\r\n"+res_body
	return final_res

def fire_request(HOST,method,path,headers,params):
	print method,HOST,path,params
	conn = httplib.HTTPSConnection(HOST)
    	conn.request(method, path, params, headers)
    	response = conn.getresponse()
    	return craft_res(response.status,response.reason,response.version,response.getheaders(),response.read())

def parsebody(bdy):				
	bodypart = bdy.split('&',bdy.count('&'))
	encode_body = {}			
	for i in range(0, bdy.count('&')+1):				
		encode_body[bodypart[i].split('=',1)[0]] = bodypart[i].split('=',1)[1]
	return encode_body
def parseheader(head,body):
	c1 = head.split('\n',head.count('\n'))
	method = c1[0].split(' ',2)[0]				
	path = c1[0].split(' ',2)[1]
	headers = {}
	for i in range(1, head.count('\n')+1):
		c1[i] = c1[i].replace('\r','')
		slice1 = c1[i].split(': ',1)
		headers[slice1[0]] = slice1[1]
	if body != "":
		body = parsebody(body)
		body = urllib.urlencode(body)
	HOST = headers['Host']
	return HOST,method,path,headers,body
def send(r_header,r_body):
	info = parseheader(r_header,r_body)
	return fire_request(info[0],info[1],info[2],info[3],info[4])

class MyTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
        	self.data = self.request.recv(1024).strip()	
        	rcvd = self.data
		if rcvd[:3] == "POS":
			post = rcvd.split('\r\n\r\n',1)
			all = send(post[0],post[1])
		else:
			all = send(rcvd,"")
		self.request.sendall(all)
if __name__ == "__main__":
	HOST, PORT = '', 8080
    	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	print "[*] Proxy Server Started(Tunneling HTTP to HTTPS).Listening on",PORT
	server.serve_forever()
