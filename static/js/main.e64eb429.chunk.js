(this["webpackJsonpcovid-vaccine-finder"]=this["webpackJsonpcovid-vaccine-finder"]||[]).push([[0],{140:function(e,t,a){},141:function(e,t,a){},153:function(e,t,a){"use strict";a.r(t);var n=a(0),i=a.n(n),c=a(12),r=a.n(c),o=(a(140),a(141),a(7)),s=a(101),l=a(43),d=a(44),u=a(56),f=a(55),h=a(102),j=a(203),v=a(108),b=a.n(v),p=a(109),x=a.n(p),O=a(84),m=a.n(O),y=m.a.mark(g);function g(e){var t;return m.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:t=0;case 1:if(!(t<e.length)){a.next=7;break}return a.next=4,[t,e[t]];case 4:t+=1,a.next=1;break;case 7:case"end":return a.stop()}}),y)}var k=a(74),N=a(13),w=[{field:"id",headerName:"id",hide:!0},{field:"available",headerName:"Available",flex:.25,renderCell:function(e){return Object(N.jsx)(j.a,{href:e.getValue("link"),children:"yes"===e.value?Object(N.jsx)(b.a,{varient:"outlined",style:{color:k.a[500]}}):Object(N.jsx)(x.a,{varient:"outlined",color:"error"})})}},{field:"provider",headerName:"Provider",flex:.25},{field:"store_name",headerName:"Store Name",flex:.25},{field:"store_address",headerName:"Store Address",flex:.25,valueGetter:function(e){return"".concat(e.value,", ").concat(e.getValue("store_city"))}},{field:"store_city",headerName:"Store City",flex:.25,hide:!0},{field:"vaccine_types",headerName:"Vaccine Types",flex:.25,valueGetter:function(e){return null!==e.value?"".concat(e.value):"N/A"}},{field:"doses_available",headerName:"Doses Available",flex:.25,valueGetter:function(e){return null!==e.value?"".concat(e.value):"N/A"}},{field:"link",headerName:"Link",flex:1,hide:!0}],C=[{field:"available",sort:"desc"}],L=function(e){Object(u.a)(a,e);var t=Object(f.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).getData=function(){fetch("data.json",{headers:{"Content-Type":"application/json",Accept:"application/json"}}).then((function(e){return e.json()})).then((function(e){var t,a=Object(s.a)(g(e));try{for(a.s();!(t=a.n()).done;){var i=Object(o.a)(t.value,2),c=i[0];i[1].id=c}}catch(r){a.e(r)}finally{a.f()}n.setState({data:e,tableLoading:!1})}))},n.state={data:[],tableLoading:!0},n}return Object(d.a)(a,[{key:"componentDidMount",value:function(){this.getData()}},{key:"render",value:function(){return Object(N.jsx)(h.a,{rows:this.state.data,columns:w,autoHeight:!0,loading:this.state.tableLoading,sortModel:C})}}]),a}(i.a.Component),A=a(110),D=a.n(A),M=function(e){Object(u.a)(a,e);var t=Object(f.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).getLastUpdated=function(){fetch("last-updated.json",{headers:{"Content-Type":"application/json",Accept:"application/json"}}).then((function(e){return e.json()})).then((function(e){n.setState({lastUpdated:D.a.unix(e.last_updated).format("YYYY-MM-DDTHH:mm:ss")})}))},n.state={lastUpdated:null},n}return Object(d.a)(a,[{key:"componentDidMount",value:function(){this.getLastUpdated()}},{key:"render",value:function(){return Object(N.jsx)("div",{children:Object(N.jsxs)("h2",{children:["Last updated at ",this.state.lastUpdated," "]})})}}]),a}(i.a.Component),S=a(111),T=a.n(S);function _(){return Object(N.jsx)(j.a,{href:"/covid-vaccine-finder/feed.xml",children:Object(N.jsx)(T.a,{})})}var U=a(206),F=a(51),I=a(200),P=a(204),Y=a(205);var G=function(){var e=Object(P.a)("(prefers-color-scheme: dark)"),t=i.a.useMemo((function(){return Object(F.a)({palette:{type:e?"dark":"light"}})}),[e]);return Object(N.jsxs)(I.a,{theme:t,children:[Object(N.jsxs)("div",{className:"App",children:[Object(N.jsx)(Y.a,{}),Object(N.jsx)(M,{}),Object(N.jsxs)(U.a,{severity:"info",children:[Object(N.jsx)(_,{})," Updates published when available vacccine is detected"]}),Object(N.jsx)(U.a,{severity:"info",children:"Icons are clickable; click to be redirected to provider's website"}),Object(N.jsx)(L,{})]}),Object(N.jsxs)("footer",{children:[Object(N.jsxs)(U.a,{severity:"info",children:["Find a bug? Contact me by",Object(N.jsx)("a",{href:"https://github.com/kirkhansen/covid-vaccine-finder/issues/new",children:" making an issue."})]}),Object(N.jsx)(U.a,{severity:"warning",children:"These data are collected via web scraping from various sources and may be out of date or inaccurate. It's also not officially supported by any of the above providers. Please continue to check with all your providers for appointment availability."})]})]})},H=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,208)).then((function(t){var a=t.getCLS,n=t.getFID,i=t.getFCP,c=t.getLCP,r=t.getTTFB;a(e),n(e),i(e),c(e),r(e)}))};r.a.render(Object(N.jsx)(i.a.StrictMode,{children:Object(N.jsx)(G,{})}),document.getElementById("root")),H()}},[[153,1,2]]]);
//# sourceMappingURL=main.e64eb429.chunk.js.map