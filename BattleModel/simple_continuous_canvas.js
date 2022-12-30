//https://github.com/projectmesa/mesa/blob/main/examples/boid_flockers/boid_flockers/simple_continuous_canvas.js


const ContinuousVisualization = function(width, height, context) {
	this.draw = function(objects) {
		for (const p of objects) {
			if (p.Shape === "rect")
			{
				this.drawRectangle(p.x, p.y, p.w, p.h, p.Color, p.Filled);
			}
			if (p.Shape === "circle")
			{
				this.drawCircle(p.x, p.y, p.r, p.Color, p.Filled);
			}
			if (p.Shape === "triangle")
			{
				this.drawTriangle(p.x, p.y, p.a, p.Color, p.Filled);
			}
			if (p.Shape === "polygon")
			{
				this.drawPolygon(p.list_of_points, p.Color, p.Filled);
			}
		}
	};

	this.drawPolygon = function (list_of_points, Color, Filled) {

		context.beginPath();
		context.moveTo(list_of_points[0][0], list_of_points[0][1]);

		for (let i=1; i<list_of_points.length; i+=1)
		{
			context.lineTo(list_of_points[i][0], list_of_points[i][1]);
		}

		context.closePath();

		context.strokeStyle = Color;
		context.stroke();

		if (Filled) {
			context.fillStyle = Color;
			context.fill();
		}

	};

	this.drawCircle = function(x, y, radius, color, fill) {
		const cx = x * width;
		const cy = y * height;
		const r = radius;

		context.beginPath();
		context.arc(cx, cy, r, 0, Math.PI * 2, false);
		context.closePath();

		context.strokeStyle = color;
		context.stroke();

		if (fill) {
			context.fillStyle = color;
			context.fill();
		}

	};

	this.drawRectangle = function(x, y, w, h, color, fill) {
		context.beginPath();
		const dx = w * width;
		const dy = h * height;

		// Keep the drawing centered:
		const x0 = (x*width) - 0.5*dx;
		const y0 = (y*height) - 0.5*dy;

		context.strokeStyle = color;
		context.fillStyle = color;
		if (fill)
			context.fillRect(x0, y0, dx, dy);
		else
			context.strokeRect(x0, y0, dx, dy);
	};

	this.drawTriangle = function (x, y, a, color, fill) {
		const cx = x * width;
		const cy = y * height;
		const tri_height = a;

		context.beginPath();

		context.moveTo(cx, cy);
        context.lineTo(cx + a, cy);
        context.lineTo(cx + a/2, cy-tri_height);
		context.closePath();

		context.strokeStyle = color;
		context.stroke();

		if (fill) {
			context.fillStyle = color;
			context.fill();
		}

	};

	this.resetCanvas = function() {
		context.clearRect(0, 0, width, height);
		context.beginPath();
	};
};

const Simple_Continuous_Module = function(canvas_width, canvas_height) {
	// Create the element
	// ------------------

  const canvas = document.createElement("canvas");
  Object.assign(canvas, {
    width: canvas_width,
    height: canvas_height,
    style: 'border:1px dotted'
  });
	// Append it to body:
  document.getElementById("elements").appendChild(canvas);

	// Create the context and the drawing controller:
	const context = canvas.getContext("2d");
	const canvasDraw = new ContinuousVisualization(canvas_width, canvas_height, context);

	this.render = function(data) {
		canvasDraw.resetCanvas();
		canvasDraw.draw(data);
	};

	this.reset = function() {
		canvasDraw.resetCanvas();
	};
};