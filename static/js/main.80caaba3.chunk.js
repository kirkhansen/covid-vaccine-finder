(this["webpackJsonpcovid-vaccine-finder"]=this["webpackJsonpcovid-vaccine-finder"]||[]).push([[0],{140:function(e,t,a){},141:function(e,t,a){},153:function(e,t,a){"use strict";a.r(t);var n=a(0),c=a.n(n),r=a(12),i=a.n(r),o=(a(140),a(141),a(7)),s=a(101),l=a(43),d=a(44),u=a(56),f=a(55),j=a(102),h=a(203),v=a(108),b=a.n(v),p=a(109),x=a.n(p),O=a(84),m=a.n(O),g=m.a.mark(y);function y(e){var t;return m.a.wrap((function(a){for(;;)switch(a.prev=a.next){case 0:t=0;case 1:if(!(t<e.length)){a.next=7;break}return a.next=4,[t,e[t]];case 4:t+=1,a.next=1;break;case 7:case"end":return a.stop()}}),g)}var k=a(74),N=a(15),C=[{field:"id",headerName:"id",hide:!0},{field:"available",headerName:"Available",flex:.25,renderCell:function(e){return Object(N.jsx)(h.a,{href:e.getValue("link"),children:"yes"===e.value?Object(N.jsx)(b.a,{varient:"outlined",style:{color:k.a[500]}}):Object(N.jsx)(x.a,{varient:"outlined",color:"error"})})}},{field:"provider",headerName:"Provider",flex:.25},{field:"store_name",headerName:"Store Name",flex:.25},{field:"store_address",headerName:"Store Address",flex:.25,valueGetter:function(e){return"".concat(e.value,", ").concat(e.getValue("store_city"))}},{field:"store_city",headerName:"Store City",flex:.25,hide:!0},{field:"vaccine_types",headerName:"Vaccine Types",flex:.25,valueGetter:function(e){return null!==e.value?"".concat(e.value):"N/A"}},{field:"doses_available",headerName:"Doses Available",flex:.25,valueGetter:function(e){return null!==e.value?"".concat(e.value):"N/A"}},{field:"link",headerName:"Link",flex:1,hide:!0}],L=[{field:"available",sort:"desc"}],A=function(e){Object(u.a)(a,e);var t=Object(f.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).getData=function(){fetch("data.json",{headers:{"Content-Type":"application/json",Accept:"application/json"}}).then((function(e){return e.json()})).then((function(e){var t,a=Object(s.a)(y(e));try{for(a.s();!(t=a.n()).done;){var c=Object(o.a)(t.value,2),r=c[0];c[1].id=r}}catch(i){a.e(i)}finally{a.f()}n.setState({data:e,tableLoading:!1})}))},n.state={data:[],tableLoading:!0},n}return Object(d.a)(a,[{key:"componentDidMount",value:function(){this.getData()}},{key:"render",value:function(){return Object(N.jsx)(j.a,{rows:this.state.data,columns:C,autoHeight:!0,loading:this.state.tableLoading,sortModel:L})}}]),a}(c.a.Component),D=a(110),w=a.n(D),M=function(e){Object(u.a)(a,e);var t=Object(f.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).getLastUpdated=function(){fetch("last-updated.json",{headers:{"Content-Type":"application/json",Accept:"application/json"}}).then((function(e){return e.json()})).then((function(e){n.setState({lastUpdated:w.a.unix(e.last_updated).format("YYYY-MM-DDTHH:mm:ss")})}))},n.state={lastUpdated:null},n}return Object(d.a)(a,[{key:"componentDidMount",value:function(){this.getLastUpdated()}},{key:"render",value:function(){return Object(N.jsx)("div",{children:Object(N.jsxs)("h2",{children:["Last updated at ",this.state.lastUpdated," "]})})}}]),a}(c.a.Component),S=a(111),_=a.n(S);function T(){return Object(N.jsx)(h.a,{href:"/covid-vaccine-finder/feed.xml",children:Object(N.jsx)(_.a,{})})}var U=a(206),F=a(51),Y=a(200),G=a(204),H=a(205);var I=function(){var e=Object(G.a)("(prefers-color-scheme: dark)"),t=c.a.useMemo((function(){return Object(F.a)({palette:{type:e?"dark":"light"}})}),[e]);return Object(N.jsx)(Y.a,{theme:t,children:Object(N.jsxs)("div",{className:"App",children:[Object(N.jsx)(H.a,{}),Object(N.jsx)(M,{}),Object(N.jsxs)(U.a,{severity:"info",children:[Object(N.jsx)(T,{})," Updates published when available vacccine is detected"]}),Object(N.jsx)(U.a,{severity:"info",children:"Icons are clickable; click to be redirected to provider's website"}),Object(N.jsx)(A,{})]})})},P=function(e){e&&e instanceof Function&&a.e(3).then(a.bind(null,208)).then((function(t){var a=t.getCLS,n=t.getFID,c=t.getFCP,r=t.getLCP,i=t.getTTFB;a(e),n(e),c(e),r(e),i(e)}))};i.a.render(Object(N.jsx)(c.a.StrictMode,{children:Object(N.jsx)(I,{})}),document.getElementById("root")),P()}},[[153,1,2]]]);
//# sourceMappingURL=main.80caaba3.chunk.js.map