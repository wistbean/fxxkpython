<p>这是你接下来要做得事情：</p>
<table border="1">
%for row in rows:
	<tr>
	%for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>